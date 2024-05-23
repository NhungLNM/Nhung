from matplotlib import pyplot as plt
import seaborn as sb
df = sb.load_dataset('tips')
sb.set(style='whitegrid')
# Boxplot
sb.boxplot(data = df, x = 'day', y = 'tip')
