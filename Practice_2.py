import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("penguins")

sns.lineplot(x = "bill_length_mm", y = "flipper_length_mm", data = data)
plt.show()

sns.lineplot(x = "bill_length_mm", y = "bill_depth_mm", data = data, hue = "sex", style = "sex", palette = "bone", markers=["o",">"])
plt.show()

data1 = sns.load_dataset("penguins").head(20)
sns.lineplot(x = "bill_length_mm", y = "bill_depth_mm", data = data1)
plt.show()
