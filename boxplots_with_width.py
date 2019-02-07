"""
Seaborn does not support boxplots with widths resembling the number of datapoints
in each box plot, but PyPlot does.

The following code takes a long-form dataframe and converts it to the correct
objects for the plt.boxplot function with sized widths.
"""


def long_form_to_plt_boxplot(df, x, y, full_width=0.8):
    """
    Take a long form dataframe and return an 2D array for plt.boxplot,
    along with a list of widths, resembling the number of samples
    in each dataset, and the category names.
    """
    categories = sorted(df[x].unique())
    data = [df[df[x] == s][y].dropna().tolist() for s in categories]
    widths = [len(x) for x in data]
    widths = [full_width * x / max(widths) for x in widths]
    return data, categories, widths

data, categories, widths = long_form_to_plt_boxplot(plot_data, 'x', 'y', full_width=1)

plt.figure(figsize=(8, 4))
plt.boxplot(data, widths=widths, showfliers=False)
plt.xticks(categories)
plt.xlabel('x')
plt.ylabel('y')
plt.show()