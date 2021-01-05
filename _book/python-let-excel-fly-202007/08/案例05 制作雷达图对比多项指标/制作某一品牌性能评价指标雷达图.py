import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('雷达图.xlsx')  
df = df.set_index('性能评价指标') 
df = df.T 
df.index.name = '品牌'  
def plot_radar(data, feature): 
    plt.rcParams['font.sans-serif'] = ['SimHei']  
    plt.rcParams['axes.unicode_minus'] = False  
    cols = ['动力性', '燃油经济性', '制动性', '操控稳定性', '行驶平顺性', '通过性', '安全性', '环保性']  
    colors = ['green', 'blue', 'red', 'yellow']  
    angles = np.linspace(0.1 * np.pi, 2.1 * np.pi, len(cols), endpoint = False)  
    angles = np.concatenate((angles, [angles[0]]))    
    fig = plt.figure(figsize = (8, 8)) 
    ax = fig.add_subplot(111, polar = True)
    for i, c in enumerate(feature):  
        stats = data.loc[c]  
        stats = np.concatenate((stats, [stats[0]]))  
        ax.plot(angles, stats, '-', linewidth = 6, c = colors[i], label = '%s'%(c)) 
        ax.fill(angles, stats, color = colors[i], alpha = 0.25)  
    ax.legend() 
    ax.set_yticklabels([])  
    ax.set_thetagrids(angles * 180 / np.pi, cols, fontsize = 16)
    plt.show()
    return fig
fig = plot_radar(df, ['A品牌'])
