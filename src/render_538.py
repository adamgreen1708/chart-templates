from datetime import datetime

# Create timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# File paths
latest_path = REPO_ROOT / "output" / "test_chart.png"
versioned_path = REPO_ROOT / "output" / f"test_chart_{timestamp}.png"

# Save both
fig.savefig(latest_path, dpi=300, bbox_inches="tight")
fig.savefig(versioned_path, dpi=300, bbox_inches="tight")

print(f"Saved latest chart to {latest_path}")
print(f"Saved versioned chart to {versioned_path}")