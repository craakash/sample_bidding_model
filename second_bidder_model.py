import matplotlib.pyplot as plt

# Example setup for bids and decay-weighted ROI
bids = {"Hotel A": 3.00, "Hotel B": 2.50, "Hotel C": 3.25}
weighted_revenue = {"Hotel A": 5.2, "Hotel B": 3.8, "Hotel C": 4.0}
roi_threshold = 1.5

# Function to adjust bids based on weighted ROI
def adjust_bids(bids, weighted_revenue, roi_threshold):
    adjusted_bids = {}
    rois = {}
    for hotel, bid in bids.items():
        revenue = weighted_revenue.get(hotel, 0)
        roi = revenue / bid if bid else 0
        rois[hotel] = roi
        print(f"Hotel: {hotel}, Bid: {bid}, Weighted Revenue: {revenue}, ROI: {roi}")

        # Adjust bid based on ROI performance
        if roi >= roi_threshold:
            adjusted_bids[hotel] = bid * 1.1  # Increase by 10% if ROI is satisfactory
        else:
            adjusted_bids[hotel] = bid * 0.9  # Decrease by 10% if ROI is below threshold
    return adjusted_bids, rois

adjusted_bids, rois = adjust_bids(bids, weighted_revenue, roi_threshold)
print("Adjusted Bids:", adjusted_bids)

# Plotting
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

# Plotting Original and Adjusted Bids
hotels = list(bids.keys())
original_bids = [bids[h] for h in hotels]
new_bids = [adjusted_bids[h] for h in hotels]
width = 0.35

ax[0].bar(hotels, original_bids, width, label='Original Bids')
ax[0].bar(hotels, new_bids, width, bottom=original_bids, label='Adjusted Bids', color='r')
ax[0].set_ylabel('Bid Amount ($)')
ax[0].set_title('Original vs Adjusted Bids')
ax[0].legend()

# Plotting ROI
roi_values = [rois[h] for h in hotels]
ax[1].bar(hotels, roi_values, color='g')
ax[1].axhline(y=roi_threshold, color='r', linestyle='--')
ax[1].set_ylabel('ROI')
ax[1].set_title('Return on Investment by Hotel')
ax[1].text(0, roi_threshold + 0.1, f'Threshold: {roi_threshold}', color='r')

plt.tight_layout()
plt.show()
