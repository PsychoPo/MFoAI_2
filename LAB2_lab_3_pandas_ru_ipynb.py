import pandas as pd
import matplotlib.pyplot as plt

def main():
	# 1
	data_set = pd.read_csv('data.csv')
	print(f"\nDATA_SET:\n\n{data_set}\n\n")

	# 2
	print(f"DESCRIBE:\n\n{data_set.describe()}\n\n")

	# 3
	print(f'DATA_SET.HEAD:\n\n{data_set.head(4)}\n\n')
	print(f'DATA_SET.TAIL:\n\n{data_set.tail(2)}\n\n')

	# 4
	data_dict = pd.read_fwf('DataDictionary-ru.txt')
	print(f"DATA_DICT:\n\n{data_dict}\n\n")

	# 5
	a = data_set['DebtRatio']
	b = data_set['MonthlyIncome']
	data_set['DebtRatio'] = a*b
	print(f"DATA_SET_CHANGED:\n\n{data_set}\n\n")

	# 6
	data_set.rename(columns={'DebtRatio':'Debt'}, inplace=True)
	print(f"DATA_SET_RENAMED:\n\n{data_set.columns.tolist()}\n\n")

	# 7
	mean_month = data_set['MonthlyIncome'].mean()
	# prod = pd.read_csv('data.csv')
	# prod.loc[prod['MonthlyIncome'].isnull()].loc['MonthlyIncome'] = mean_month
	print(f"MEAN_MONTH:\n\n{mean_month}\n\n")

	data_set['MonthlyIncome'] = data_set['MonthlyIncome'].fillna(mean_month)
	data_set.to_csv('prod.csv')
	print(f"PROD:\n\n{pd.read_csv('prod.csv')}\n\n")

	# 8
	mean_dep = data_set['SeriousDlqin2yrs'].groupby(data_set['NumberOfDependents']).mean()
	print(f"MEAN_DEP:\n\n{mean_dep}\n\n")
	mean_estate = data_set['SeriousDlqin2yrs'].groupby(data_set['NumberRealEstateLoansOrLines']).mean()
	print(f"MEAN_ESTATE:\n\n{mean_estate}\n\n")

	# 9a
	zeroDebts = data_set.loc[data_set["SeriousDlqin2yrs"] == 0]
	moreThanZeroDebts = data_set.loc[data_set["SeriousDlqin2yrs"] > 0]

	fig1 = plt.figure()
	ax1 = fig1.subplots()
	ax1.scatter(zeroDebts['age'], zeroDebts["Debt"], c="blue")
	ax1.scatter(moreThanZeroDebts['age'], moreThanZeroDebts["Debt"], c="red")
	ax1.set_title('First')

	# 9b
	fig2 = plt.figure()
	ax2 = fig2.subplots()

	plt.xlim([0, 25000])

	zeroDebts['MonthlyIncome'].plot.kde(ax=ax2, label="Без серьезных задолжностей", color="b")
	moreThanZeroDebts['MonthlyIncome'].plot.kde(ax=ax2, label="С серьезными задолжностями", color="r")
	ax2.set_title('Зарплата')

	# 9c*
	incomeNoMoreThan25K = data_set.loc[data_set["MonthlyIncome"] <= 25000]

	fig3 = plt.figure()
	ax3 = fig3.subplots()
	# судя по данным отсутствует
	plt.xlim([16, 100])
	plt.ylim([0, 25000])
	ax3.plot(incomeNoMoreThan25K['age'],incomeNoMoreThan25K['MonthlyIncome'], 'o')
	ax3.set_title("Взаимосвязь возраста и зарплаты")

	fig4 = plt.figure()
	ax4 = fig4.subplots()
	# Нормальное(Гаусса) распределение?
	plt.xlim([16, 100])
	plt.ylim([0, 20])
	yint = range(int(incomeNoMoreThan25K['NumberOfDependents'].min()), int(incomeNoMoreThan25K['NumberOfDependents'].max())+20)
	plt.yticks(yint) 
	ax4.plot(incomeNoMoreThan25K['age'],incomeNoMoreThan25K['NumberOfDependents'], 'o')
	ax4.set_title("Взаимосвязь возраста и числа иждивенцев")

	fig5 = plt.figure()
	ax5 = fig5.subplots()
	# судя по данным отсутствует
	plt.xlim([0, 25000])
	plt.ylim([0, 20])
	yint = range(int(incomeNoMoreThan25K['NumberOfDependents'].min()), int(incomeNoMoreThan25K['NumberOfDependents'].max())+20)
	plt.yticks(yint)
	ax5.plot(incomeNoMoreThan25K['MonthlyIncome'],incomeNoMoreThan25K['NumberOfDependents'], 'o')
	ax5.set_title("Взаимосвязь зарплаты и числа иждивенцев")

	plt.show()

if __name__ == "__main__":
	main()