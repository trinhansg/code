import matplotlib.pyplot as plt
import numpy as np

girls_grades = np.random.randint(0, 50, 50)
boys_grades = np.random.randint(0, 50, 50)
grades_range = np.arange(50)

plt.scatter(grades_range, girls_grades, color='r', s=girls_grades*10, label='girls')
plt.scatter(grades_range, boys_grades, color='g', s=boys_grades*10, label='boys')
plt.xlabel('Grades Range')
plt.ylabel('Grades Scored')
plt.title('scatter plot')
plt.legend(loc=4)
plt.show()