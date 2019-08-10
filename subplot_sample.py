import matplotlib.pyplot as plt
fig, axs = plt.subplots(5,2,figsize=(10,15))
for i,data in enumerate(datas):
    axs[i//2,i%2].plot(x=data.x, y=data.y,label=data.label)
    axs[i//2,i%2].set_title(data.title)
    axs[i//2,i%2].legend()
    axs[i//2,i%2].set_ylabel(data.y_label)
    axs[i//2,i%2].set_xlabel(data.x_label)
    plt.tight_layout()
plt.savefig("/tmp/test.png")
