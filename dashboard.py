import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("==================================================")
print("  VIRTUALWORKS LABS - HIGH-TECH COMMAND CONSOLE   ")
print("==================================================\n")

# [Step 1] Load real-time performance database logs
df = pd.read_csv('executive_kpis.csv')

# [Step 2] Configure High-Tech Dark Palette Architecture
plt.style.use('dark_background')
fig = plt.figure(figsize=(16, 9), facecolor='#0D0E15') # Deep space cyber backdrop

# FIXED LINE: Restored clean layout grid tracking limits
gs = fig.add_gridspec(2, 3, width_ratios=[1, 1.5, 1], height_ratios=[1.2, 1])

# --- PANEL 1: Left Column - Core Single Value Telemetry Cards ---
ax_left = fig.add_subplot(gs[:, 0], facecolor='#121420')
ax_left.axis('off')
ax_left.text(0.1, 0.90, '$8,903', fontsize=42, fontweight='bold', color='#00FFCC') # Glowing Neon Cyan
ax_left.text(0.1, 0.83, 'MRR RUNTIME LEVEL', fontsize=11, color='#6B7280', fontweight='bold')

ax_left.text(0.1, 0.65, '$456', fontsize=34, fontweight='bold', color='#FFFFFF')
ax_left.text(0.1, 0.59, 'DAILY INFLOW RATIO', fontsize=11, color='#6B7280', fontweight='bold')

ax_left.text(0.1, 0.40, '-$265', fontsize=34, fontweight='bold', color='#FF0055') # Laser Hot Pink
ax_left.text(0.1, 0.34, 'PREVIOUS INTERVAL GAP', fontsize=11, color='#6B7280', fontweight='bold')

# Stream Section: Recent Operations Feed
feed_text = 'SYSTEM_LOG: Robinson (Premium) -> +$355 ACTIVE\n' \
            'SYSTEM_LOG: Reece (Basic)     -> +$189 ACTIVE'
ax_left.text(0.1, 0.18, feed_text, fontsize=10, color='#00FFCC', family='monospace', va='center')
ax_left.set_title('// MRR PERFORMANCE PROFILE', color='#00FFCC', fontsize=12, fontweight='bold', loc='left', pad=15)

# --- PANEL 2: Top Center - Cumulative MRR Added Line Plot ---
ax_line = fig.add_subplot(gs[0, 1], facecolor='#121420')
ax_line.plot(df['date'], df['mrr_this_month'], color='#00FFCC', linewidth=3.5, marker='o', markersize=6, label='CURRENT STREAM')
ax_line.plot(df['date'], df['mrr_last_month'], color='#39FF14', linewidth=2.5, linestyle='--', label='BASELINE TRACK') # Fluorescent Green
ax_line.set_title('// NET MRR PROGRESSION INDEX', fontsize=12, fontweight='bold', color='#FFFFFF', loc='left', pad=12)
ax_line.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: f"${int(x/1000)}K" if x>=0 else f"-${int(abs(x)/1000)}K"))
ax_line.legend(frameon=False, loc='upper left', fontsize=10)
ax_line.grid(True, color='#1F2937', linestyle='-', alpha=0.8, linewidth=1.2) # High-contrast terminal grid

# --- PANEL 3: Bottom Center - Grouped Columns Signups Chart ---
ax_bar = fig.add_subplot(gs[1, 1], facecolor='#121420')
x = np.arange(len(df['week']))
width = 0.32
ax_bar.bar(x - width/2, df['signups'], width, label='INGRESS CONVERSION', color='#00BFFF', alpha=0.9)
ax_bar.bar(x + width/2, df['day2_active'], width, label='RETENTION MATRIX', color='#FF0055', alpha=0.9)
ax_bar.set_title('// SIGNAL INGRESS & RETENTION VECTOR', fontsize=12, fontweight='bold', color='#FFFFFF', loc='left', pad=12)
ax_bar.set_xticks(x)
ax_bar.set_xticklabels(df['week'], color='#9CA3AF', fontweight='bold', fontsize=10)
ax_bar.legend(frameon=False, loc='upper right', fontsize=10)
ax_bar.grid(True, color='#1F2937', linestyle='-', alpha=0.8, linewidth=1.2)

# --- PANEL 4: Right Column - Operational Summary Matrix Sidebar ---
ax_right = fig.add_subplot(gs[:, 2], facecolor='#121420')
ax_right.axis('off')
right_metrics = [
    ('$984.6K', 'TOTAL ASSET VALUE'), ('9,875', 'PREMIUM SUBSCRIPTIONS'), 
    ('23.5K', 'STANDARD FREE TIERS'), ('5,145', 'MONTHLY SIGNUP RATE'),
    ('4,581', 'CORE LIVE USER MATRIX'), ('51.1%', 'DAU / MAU COEFFICIENT')
]
y_pos = 0.88
for value, title in right_metrics:
    ax_right.text(0.1, y_pos, value, fontsize=28, fontweight='bold', color='#FFFFFF')
    ax_right.text(0.1, y_pos - 0.04, title, fontsize=10, color='#6B7280', fontweight='bold')
    y_pos -= 0.16
ax_right.set_title('// GLOBAL NETWORK STATE', color='#00FFCC', fontsize=12, fontweight='bold', loc='left', pad=15)

# Style structural tech panels
for ax in [ax_line, ax_bar]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#1F2937')
    ax.spines['bottom'].set_color('#1F2937')
    ax.tick_params(colors='#9CA3AF', labelsize=10)

plt.suptitle('CRITICAL CORE SYSTEMS INTERFACE: OPERATIONS STREAM', fontsize=14, fontweight='bold', color='#FFFFFF', y=0.97)
plt.tight_layout(pad=3.5)

# Save the tech-mode image asset
plt.savefig('executive_dashboard.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()

print("\n High-tech command console complete! Saved as 'executive_dashboard.png'")
