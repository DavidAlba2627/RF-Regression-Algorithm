import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Compute and plot the MAE and RMSE metrics.
def plot_metrics(y_test, y_pred):
    """
    Parameters:
    - y_test: The true values.
    - y_pred: The predicted values.
    """

    # Calculating MAE and RMSE
    MAE = mean_absolute_error(y_test, y_pred)
    RMSE = mean_squared_error(y_test, y_pred, squared=False)

    # Creating the figure
    fig, ax = plt.subplots(figsize=(9, 6), facecolor='#F5F5F5')
    plt.rcParams['font.size'] = '14'
    ax.set_facecolor('#F5F5F5')

    # Creating the bar for MAE
    bar1 = ax.bar(0.25, MAE, color='firebrick', width=0.23)[0]
    # Adding the value of the MAE on top of the bar
    yval1 = bar1.get_height()
    ax.text(bar1.get_x() + bar1.get_width()/2, yval1, round(yval1, 2), ha='center', va='bottom', fontsize=16)

    # Creating the bar for RMSE
    bar2 = ax.bar(0.75, RMSE, color='seagreen', width=0.23)[0]
    # Adding the value of the RMSE on top of the bar
    yval2 = bar2.get_height()
    ax.text(bar2.get_x() + bar2.get_width()/2, yval2, round(yval2, 2), ha='center', va='bottom', fontsize=16)

    # Adding ticks and title
    ax.set_xticks([0.25, 0.75])
    ax.set_xticklabels(['MAE', 'RMSE'], fontsize=16)
    ax.set_title('Metrics for Random Forest', fontsize=18)
    ax.set_ylim([0, 70])
    ax.set_xlim([0, 1])

    # Display the plot
    plt.show()
