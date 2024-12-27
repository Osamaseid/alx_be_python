from scipy import stats

# Calculate the mean and standard deviation
data = [1, 2, 3, 4, 5]
mean = stats.tmean(data)
std_dev = stats.tstd(data)
print("Mean:", mean, "Standard Deviation:", std_dev)