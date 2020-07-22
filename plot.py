


def bar_plot(x, y, x_label, y_label, horizontal = False):
		fig,ax = plt.subplots(figsize = (10,6))
		if horizontal:
			ax.barh(y,x, align = 'center')
			ax.set_xlabel(x_label)
			ax.set_ylabel(y_label)
		else
			ax.bar(x,y, width = .35)
			ax.set_xlabel(x_label)
			ax.set_ylabel(y_label)


def multi_bar(x, y,rows, columns,  title, xlabel, ylabel,):
	fig, axs = plt.subplots(rows, columns figsize =(10,6))
	for i, ax in enumerate(axs.flatten()):
  	ax.bar(x,y[i])
    ax.set_title(title[i])
		ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
	plt.tight_layout()


def hist_plot(x,x_label,y_label):
		fig, ax = plt.subplots(10,6)
		ax.hist(x)
		ax.set_xlabel(x_label)
		ax.set_ylable(y_label)

def box_plot(data,xticklabels, label, showfliers = False, vert = False):
		fig, ax = plt.subplots(figsize = (10,6))
			ax.grid(False)
		ax.boxplot(data, showfliers, vert = False)
		if vert:
			ax.set_xticklabels(xticklabels)
			ax.set_ylabel(ylabel)
		else:
			ax.set_yticklabels(xticklabels)
			ax.set_xlabel(label)

def side_bar(x, y, xlabel, y_label,horizontal = Flase):
		fig,ax = plt.subplots(figsize = (10,6))
		ax.set_xlabel(xlabel)
		ax.set_ylabel(ylabel)
		for i in len(x):
			ax.bar(x,y[i], width = .35)

	def region(x):
    region = {0:['Arizona', 'Colorodo', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming', 'Alaska', 'California', 'Hawaii','Oregon', 'Washington'], 1: ['Deleware', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virginia', 'District of Columbia', 'West Virginia','Alabama', 'Kentucky','Mississippi','Tennessee','Arkansas', 'Louisiana','Oklahoma','Texas'],
		2: ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin','Iowa', 'Kansas','Minnesota','Missouri','Nebraska', 'North Dakota', 'South Dakota'],
		3: ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont', 'New Jersey', 'New York', 'Pennsylvania']}
    numerical = {0: 'West', 1:'South', 2: 'Midwest', 3:'Northeast'}
    if x in region[0]:
        return numerical[0]
    elif x in region[1]:
        return numerical[1]
    elif x in region[2]:
        return numerical[2]
    else:
        return numerical[3]



	def group_by_brand(df,col1,col2):
		'''
		col1: column to be grouped with brand
		col2: column to be looked at ex. profit

		'''
		return df.groupby([col1,'Brand'])[col2]

	def brand_by_col(grouped_df, col):
		'''
		col: column of interest ex. region or state

		'''
		return [grouped_df.loc[(col,'Yeezy')],grouped_df.loc[(col,'Off-White')]]

	def brand_by_multi_col(grouped_df, lst):
		return [brand_by_col(grouped_df, col) for col in lst]


	# def region_df(df, reg_name):
	# 	return df[df['Buyer Region']== reg_name]

	def brand_count(region_df):
			return region_df.value_counts()

	def state_brand_count(df, state):
		return df[df['Buyer State']==state]['Brand'].value_counts()

	def reg_spending(reg_df):
		return reg_df.groupby('Brand')['Sale Price'].sum()

	def state_spending(grouped_df, state):
		return [grouped_df.loc[(state,'Yeezy')],grouped_df.loc[(state,'Off-White')]]

	def multi_state_spending(grouped_df, state_lst):
		return [state_spending(grouped_df, state) for state in state_lst]
