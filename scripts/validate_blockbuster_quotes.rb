#!/usr/bin/env ruby
# frozen_string_literal: true

require "date"
require "yaml"
require "uri"

ROOT = File.expand_path("..", __dir__)
EDITION_DIR = File.join(ROOT, "site", "_blockbuster_quotes")
REQUIRED_TEXT = %w[
  header film quote character performer why_today kicker connection_type
  hero_image hero_alt
].freeze
REQUIRED_QA = %w[
  run_date_verified date_link_verified quote_verified speaker_verified
  copy_deck_frozen render_checked
].freeze

errors = []
seen_dates = {}

def front_matter(path)
  raw = File.read(path, encoding: "UTF-8")
  match = raw.match(/\A---\s*\n(.*?)\n---\s*(?:\n|\z)/m)
  raise "missing YAML front matter" unless match

  YAML.safe_load(match[1], permitted_classes: [Date, Time], aliases: false) || {}
end

def iso_date(value)
  return value.to_date if value.respond_to?(:to_date)

  Date.iso8601(value.to_s)
end

def https_url?(value)
  uri = URI.parse(value.to_s)
  uri.is_a?(URI::HTTPS) && uri.host && !uri.host.empty?
rescue URI::InvalidURIError
  false
end

def square_png?(path)
  bytes = File.binread(path, 24)
  return false unless bytes.start_with?("\x89PNG\r\n\x1A\n".b)

  width, height = bytes.byteslice(16, 8).unpack("NN")
  width == height && width >= 1000
rescue Errno::ENOENT, EOFError
  false
end

Dir.glob(File.join(EDITION_DIR, "*.md")).sort.each do |path|
  name = File.basename(path)

  begin
    data = front_matter(path)

    REQUIRED_TEXT.each do |key|
      errors << "#{name}: #{key} is required" if data[key].to_s.strip.empty?
    end

    date = iso_date(data.fetch("date"))
    expected_prefix = "#{date.iso8601}-"
    errors << "#{name}: filename must begin #{expected_prefix}" unless name.start_with?(expected_prefix)
    errors << "#{name}: duplicate edition date #{date}" if seen_dates[date]
    seen_dates[date] = true

    errors << "#{name}: header must be TODAY’S BLOCKBUSTER QUOTE" unless data["header"] == "TODAY’S BLOCKBUSTER QUOTE"

    year = Integer(data.fetch("film_year"))
    errors << "#{name}: film_year is outside a plausible range" unless (1888..(Date.today.year + 1)).cover?(year)

    why_words = data["why_today"].to_s.scan(/[[:alnum:]’'-]+/).length
    errors << "#{name}: why_today must contain 35–65 words (found #{why_words})" unless (35..65).cover?(why_words)

    sources = data["sources"]
    unless sources.is_a?(Array)
      errors << "#{name}: sources must be a list"
      sources = []
    end

    sources.each_with_index do |source, index|
      unless source.is_a?(Hash)
        errors << "#{name}: source #{index + 1} must be a mapping"
        next
      end
      errors << "#{name}: source #{index + 1} needs a title" if source["title"].to_s.strip.empty?
      errors << "#{name}: source #{index + 1} must use an https URL" unless https_url?(source["url"])
    end

    date_urls = sources.filter { |source| source.is_a?(Hash) && source["role"] == "date_link" }
                       .map { |source| source["url"] }.uniq
    quote_urls = sources.filter { |source| source.is_a?(Hash) && source["role"] == "quote" }
                        .map { |source| source["url"] }.uniq
    errors << "#{name}: two independent date_link sources are required" if date_urls.length < 2
    errors << "#{name}: at least one quote source is required" if quote_urls.empty?

    qa = data["qa"]
    unless qa.is_a?(Hash)
      errors << "#{name}: qa must be a mapping"
      qa = {}
    end
    REQUIRED_QA.each do |key|
      errors << "#{name}: qa.#{key} must be true" unless qa[key] == true
    end

    image = data["hero_image"].to_s
    unless image.start_with?("/assets/blockbuster-quote/")
      errors << "#{name}: hero_image must live under /assets/blockbuster-quote/"
    end
    image_path = File.join(ROOT, "site", image.delete_prefix("/"))
    errors << "#{name}: hero image must be a square PNG of at least 1000px" unless square_png?(image_path)
  rescue KeyError => e
    errors << "#{name}: missing #{e.key}"
  rescue ArgumentError, Psych::SyntaxError => e
    errors << "#{name}: #{e.message}"
  rescue StandardError => e
    errors << "#{name}: #{e.message}"
  end
end

if errors.any?
  warn "Blockbuster Quote validation failed:"
  errors.each { |error| warn "  - #{error}" }
  exit 1
end

puts "Blockbuster Quote validation passed."
