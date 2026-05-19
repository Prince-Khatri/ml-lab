import matplotlib.pyplot as plt
# import numpy as np

# # -----------------------------------
# # Data
# # -----------------------------------
# names = [
#     "Shashank Prabhu",
#     "Varun Prabhu",
#     "Uday Prabhu",
#     "Manjunath Prabhu",
#     "Sahil Prabhu",
#     "Vishal Prabhu",
#     "Prince"
# ]

# # Studies (hours)
# studies = np.array([
#     7.0,
#     6.0,
#     6.0,
#     4.5,
#     5.5,
#     7.0,
#     8.0
# ])

# # Book Reading (minutes -> hours)
# book_reading = np.array([
#     30/60,
#     30/60,
#     35/60,
#     70/60,
#     30/60,
#     25/60,
#     30/60
# ])

# # Hearing (hours)
# hearing = np.array([
#     0,
#     15/60,
#     0,
#     2.5,
#     0,
#     45/60,
#     7/60
# ])

# # Total hours
# totals = studies + book_reading + hearing

# # -----------------------------------
# # Sort by total hours
# # -----------------------------------
# sorted_idx = np.argsort(totals)

# names = np.array(names)[sorted_idx]
# studies = studies[sorted_idx]
# book_reading = book_reading[sorted_idx]
# hearing = hearing[sorted_idx]
# totals = totals[sorted_idx]

# # -----------------------------------
# # Plot
# # -----------------------------------
# plt.figure(figsize=(14, 7))

# # Bright light colors
# study_color = "#66D9EF"     # bright cyan
# reading_color = "#FFB3C6"   # bright pink
# hearing_color = "#FFE66D"   # bright yellow

# bar_width = 0.7

# # Bars
# bars1 = plt.bar(
#     names,
#     studies,
#     width=bar_width,
#     color=study_color,
#     edgecolor='white',
#     linewidth=1.5,
#     label='Studies'
# )

# bars2 = plt.bar(
#     names,
#     book_reading,
#     bottom=studies,
#     width=bar_width,
#     color=reading_color,
#     edgecolor='white',
#     linewidth=1.5,
#     label='Book Reading'
# )

# bars3 = plt.bar(
#     names,
#     hearing,
#     bottom=studies + book_reading,
#     width=bar_width,
#     color=hearing_color,
#     edgecolor='white',
#     linewidth=1.5,
#     label='Hearing'
# )

# # -----------------------------------
# # Add values inside each block
# # -----------------------------------
# for i in range(len(names)):

#     # Studies label
#     plt.text(
#         i,
#         studies[i] / 2,
#         f"{studies[i]:.1f}",
#         ha='center',
#         va='center',
#         fontsize=10,
#         fontweight='bold'
#     )

#     # Book reading label
#     if book_reading[i] > 0:
#         plt.text(
#             i,
#             studies[i] + (book_reading[i] / 2),
#             f"{book_reading[i]:.2f}",
#             ha='center',
#             va='center',
#             fontsize=9,
#             fontweight='bold'
#         )

#     # Hearing label
#     if hearing[i] > 0:
#         plt.text(
#             i,
#             studies[i] + book_reading[i] + (hearing[i] / 2),
#             f"{hearing[i]:.2f}",
#             ha='center',
#             va='center',
#             fontsize=9,
#             fontweight='bold'
#         )

#     # Total label on top
#     plt.text(
#         i,
#         totals[i] + 0.08,
#         f"{totals[i]:.2f} h",
#         ha='center',
#         fontsize=10,
#         fontweight='bold'
#     )

# # -----------------------------------
# # Styling
# # -----------------------------------
# plt.title(
#     "Study Marathon Report- 17th May, 2026",
#     fontsize=20,
#     fontweight='bold',
#     pad=20
# )

# plt.ylabel("Hours", fontsize=13)
# plt.xticks(rotation=12, fontsize=10)
# plt.yticks(fontsize=10)

# # Grid
# plt.grid(
#     axis='y',
#     linestyle='--',
#     alpha=0.25
# )

# # Remove unnecessary borders
# ax = plt.gca()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# # Legend
# plt.legend(
#     frameon=False,
#     fontsize=11
# )

# plt.tight_layout()
# plt.show()