#!/usr/bin/env ruby
# frozen_string_literal: true

require "date"
require "yaml"
require "uri"

ROOT = File.expand_path("..", __dir__)
EDITION_DIR = File.join(ROOT, "site", "_data_lens")
RESOURCE_DIR = File.join(ROOT, "site", "assets", "data-lens", "resources", "chart-choice-guide")
REQUIRED_TEXT = %w[header title observation kicker hero_image hero_alt].freeze
REQUIRED_QA = %w[run_date_verified claim_verified sources_verified copy_deck_frozen render_checked].freeze
RESOURCE_IMAGES = %w[
  01-big-number.webp
  02-compare-categories.webp
  03-rank-the-field.webp
  04-change-over-time.webp
  05-before-vs-after.webp
  06-part-to-whole.webp
  07-relationship.webp
  08-distribution.webp
  09-contribution-to-change.webp
  10-precise-lookup.webp
  11-actual-vs-forecast.webp
  12-two-trends.webp
  13-timeline.webp
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

def square_webp?(path)
  bytes = File.binread(path, 32)
  return false unless bytes.byteslice(0, 4) == "RIFF" && bytes.byteslice(8, 4) == "WEBP"

  chunk = bytes.byteslice(12, 4)
  width, height = case chunk
                  when "VP8X"
                    [1 + bytes.getbyte(24) + (bytes.getbyte(25) << 8) + (bytes.getbyte(26) << 16),
                     1 + bytes.getbyte(27) + (bytes.getbyte(28) << 8) + (bytes.getbyte(29) << 16)]
                  when "VP8 "
                    [bytes.byteslice(26, 2).unpack1("v") & 0x3fff,
                     bytes.byteslice(28, 2).unpack1("v") & 0x3fff]
                  when "VP8L"
                    bits = bytes.byteslice(21, 4).unpack1("V")
                    [1 + (bits & 0x3fff), 1 + ((bits >> 14) & 0x3fff)]
                  else
                    return false
                  end

  width == height && width >= 1000
rescue Errno::ENOENT, EOFError, NoMethodError
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

    errors << "#{name}: header must be TODAY’S DATA LENS" unless data["header"] == "TODAY’S DATA LENS"

    sources = data["sources"]
    unless sources.is_a?(Array) && sources.any?
      errors << "#{name}: at least one source is required"
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

    qa = data["qa"]
    unless qa.is_a?(Hash)
      errors << "#{name}: qa must be a mapping"
      qa = {}
    end
    REQUIRED_QA.each do |key|
      errors << "#{name}: qa.#{key} must be true" unless qa[key] == true
    end

    image = data["hero_image"].to_s
    unless image.start_with?("/assets/data-lens/daily/")
      errors << "#{name}: hero_image must live under /assets/data-lens/daily/"
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

RESOURCE_IMAGES.each do |name|
  path = File.join(RESOURCE_DIR, name)
  errors << "chart-choice-guide/#{name}: must be a square WebP of at least 1000px" unless square_webp?(path)
end

unexpected = Dir.glob(File.join(RESOURCE_DIR, "*.*")).map { |path| File.basename(path) } - RESOURCE_IMAGES
unexpected.each { |name| errors << "chart-choice-guide/#{name}: unexpected resource image" }

if errors.any?
  warn "Data Lens validation failed:"
  errors.each { |error| warn "  - #{error}" }
  exit 1
end

puts "Data Lens validation passed."
