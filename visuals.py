import matplotlib.pyplot as plt


def lineplot_image(data: list):
    fig, ax = plt.subplots()

    ax.plot(data, color = "purple")
    ax.set_title("Heart Rate Data Pipeline")
    ax.set_xlabel("Minutes")
    ax.set_ylabel("Heart Rate (bpm)")
    fig.savefig("images/hr_lineplot")

    plt.close()





