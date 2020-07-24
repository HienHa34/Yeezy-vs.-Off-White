# Yeezy-vs.-Off-White

Background:
StockX is company that provides a platform for people to buy and sell shoes, clothes, and collectables. StockX has a bidding and buy it now option much like ebay. The platform offers information such as when the last time the shoe was sold, how much it was sold for, and the size. 

Dataset: 
The dataset came from a sample of StockX transactions from September 2017 to Frebruary 2019. There are 99956 rows and 8 columns, includes sale price, retail price, order date, release date, shoe size, buyer region, sneaker name and brand. There were 76162 Yeezy shoes and 27794 Off-White shoes. 

Goal: 
Of all the columns in the dataset, the sale price is the most important to both the sellers and buyers,therefore, my goal is to analyze the sale price between the two brands, Yeezy(adidas) and Off-White (Nike). This would let sellers and buyers know what to expect when they plan on selling or purchasing the Yeezy or Off-white shoes. 

Hypothesis Test:
I conducted a Welch's t-test because the two samples, Yeezy and Off-White, had big difference in sample sizes, so the variances are unequal. My null hypothesis is the mean of the sale price of Yeezy is the same as the mean sale price of Off-White and alternate hypothesis is that the means are not equal. The alpha of the hypothesis test is .05. The results of the hypothesis is a p-value of 0.0. It's is 0.0 because the p-value is too small to have significant figures. With the p-value of 0.0, I will reject the null hypothesis that the mean sale price of Yeezy is the same the mean sale price of Off-White.

