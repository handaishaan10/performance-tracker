
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_student_performance(file_path):
   
    data = pd.read_csv(r"C:\Users\handa\Downloads\student_performance_sample.csv")

    
    print("Data preview:\n", data.head())
    
   
    print("\nBasic Statistics per subject:")
    print(data.describe())

    data['Total'] = data.iloc[:, 1:].sum(axis=1)
    data['Average'] = data['Total'] / (len(data.columns) - 1)

   
    print("\nTop performers:")
    print(data.nlargest(5, 'Average')[['Student', 'Average']])

   
    subject_avg = data.iloc[:, 1:].mean()
    print("\nAverage scores per subject:")
    print(subject_avg)

    highest_performance = subject_avg.idxmax()
    lowest_performance = subject_avg.idxmin()
    print(f"\nHighest average score: {highest_performance}")
    print(f"Lowest average score: {lowest_performance}")

    
    plt.figure(figsize=(10, 6))      #Plotting of graph

  
    sns.barplot(x=subject_avg.index, y=subject_avg.values)
    plt.title('Average Scores by Subject')
    plt.xlabel('Subjects')
    plt.ylabel('Average Score')
    plt.show()

    
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Average'], kde=True)
    plt.title('Distribution of Student Average Scores')
    plt.xlabel('Average Score')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Between Subjects')
    plt.show()


file_path = 'student_performance.csv'
analyze_student_performance(r"C:\Users\handa\Downloads\student_performance_sample.csv")

