import mne
import matplotlib
from matplotlib import pyplot as plt
import numpy as np


def plot_epochs(epochs, nchans, ch_names, color='b', label='spkr', show=True, vmin_max=None):
    '''
    Function that plots the averaged epoched data for each channel as a grid so you can 
    see all channels at once.
    
    Inputs:
        epochs [obj] : MNE epochs object
        nchans [int] : number of channels to plot
        ch_names [list] : channel names 
        color [str, hex, tuple]: color for ERP traces
        label [str] : label for the ERP (could be epoch type/annotation type) 
        show [bool] : whether to show the figure or not
        vmin_max [list] : list of ylim min and max, e.g. [-0.5, 0.5]
        
    '''
    
    # Get the data as an array
    eps = epochs.get_data()
    
    # Find the maximum across the whole dataset, helps with scaling the plots
    emax = np.abs(epochs.average().data).max()
    
    # Determine how many rows and columns we'll need in our subplots grid
    # based on the number of channels. 
    nrows = int(np.floor(np.sqrt(nchans)))
    ncols = int(np.ceil(nchans/nrows))
    
    # Loop through all electrode channels
    for ch in np.arange(nchans):
        plt.subplot(nrows, ncols, ch+1)
        
        # Get the average response across trials for this particular channel
        erp = eps[:,ch,:].mean(0)
        
        # Get the standard error across trials
        erpstderr = eps[:,ch,:].std(0)/np.sqrt(eps.shape[0])
        
        # Plot transparent shaded standard error in the [color] you choose
        ybottom = erp - erpstderr
        ytop = erp + erpstderr
        plt.fill_between(epochs.times, ybottom.ravel(), ytop.ravel(),
                         alpha=0.5, color=color)
        
        # Plot the average epoch on top in the same color
        plt.plot(epochs.times, erp, color=color, label=label)
        
        # Plot the x and y origins
        plt.axvline([0], color='k', linewidth=0.5)
        plt.axhline([0], color='k', linewidth=0.5)
        
        # If we haven't explicitly set ylimits with vmin/vmax, use 
        # the maximum of the data and 50% more so the whole thing 
        # fits nicely 
        if vmin_max is None:
            plt.gca().set_ylim([-emax*1.5, emax*1.5])
        else:
            plt.gca().set_ylim([vmin_max[0], vmin_max[1]])
            
        # Only show the ticks for the 0th plot, otherwise this gets
        # hard to see/read
        if ch != 0:
            plt.gca().set_xticks([])
            plt.gca().set_yticks([])
        else:
            plt.ylabel('Z-score')
        
        # Write the name of the channel in the plot -- you could also
        # use plt.title() but sometimes that makes everything look
        # a little squashed
        plt.text(0.5, 0.25, ch_names[ch], 
            horizontalalignment='center', verticalalignment='center',
            transform=plt.gca().transAxes, fontsize=8)
    
    # Plot ticks at meaningful times (the min, 0, and max in seconds)
    plt.gca().set_xticks([epochs.tmin, 0, epochs.tmax])
    plt.xlabel('Time (s)')
    plt.legend()
    #plt.tight_layout()
    if show:
        plt.show()