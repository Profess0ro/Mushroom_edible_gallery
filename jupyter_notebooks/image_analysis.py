import os
import pandas as pd
import matplotlib.pyplot as plt


def images_percentage_distribution(image_dirs, save_path=None):

    # Creates a list that collects images per specie
    images_per_specie = {}
    for species in os.listdir(image_dirs):
        species_path = os.path.join(image_dirs, species)
        if os.path.isdir(species_path):
            images_per_specie[species] = len([img for img in os.listdir(species_path) if img.endswith(('.png', 'jpg', 'jpeg'))])
            

    # Convert this list to a dataframe
    df = pd.DataFrame(list(images_per_specie.items()), columns=['Species', 'Count'])

    # Calculate the percentage of images per specie
    df['Percentage'] = (df['Count'] / df['Count'].sum()) * 100

    # Calculate the highest, the lowest and mean value of the distribution
    highest = df.loc[df['Percentage'].idxmax()]
    lowest = df.loc[df['Percentage'].idxmin()]
    mean_percentage = df['Percentage'].mean()
    mean_count = df['Count'].mean()


    # Create a barplot to visualize this distibution of images per specie
    plt.figure(figsize=(15, 8))
    plt.bar(df['Species'], df['Percentage'], color='skyblue')
    plt.axhline(y=mean_percentage, color='r', linestyle='--')
    plt.xlabel('Species')
    plt.ylabel('Percentage (%)')
    plt.title('Percentage distribution of images per specie')
    plt.xticks(rotation=90)

    # Adds extra text to the top of the barplot
    plt.gcf().text(0.40, 0.85, f"Mean percentage: {mean_percentage:.2f}% ({mean_count:.0f} images)", fontsize=10)
    plt.gcf().text(0.40, 0.82, f"Highest percentage: {highest['Species']} - {highest['Percentage']:.2f}% ({highest['Count']} images)", fontsize=10)
    plt.gcf().text(0.40, 0.79, f"Lowest percentage: {lowest['Species']} - {lowest['Percentage']:.2f}% ({lowest['Count']} images)", fontsize=10)

    # If save_path is given it will save an image of the barplot at the given path
    if save_path:
        plt.savefig(save_path, format='png', bbox_inches='tight')
    
    # Shows the barplot
    plt.tight_layout()
    plt.show()
    
    return df
    