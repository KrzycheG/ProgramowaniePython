import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.DataFrame({'Months': ['I 2022', 'II 2022', 'III 2022', 'IV 2022', 'V 2022'],
                          'Profit': [15, 35, 5, 35, 15],
                          'Loss': [25, 25, 35, 10, 25]})

figure, axis = plt.subplots(2, 3)
profitLossSum = [dataframe['Profit'].sum(), dataframe['Loss'].sum()]



axis[0, 0].pie(profitLossSum,labels=['Profit','Loss'],autopct='%1.1f%%',colors=['Green','Red'])
axis[0, 0].set_title("Win Loss Overall")


axis[0, 1].bar(['Profit', 'Loss'], [dataframe._get_value(0, 'Profit'), dataframe._get_value(0, 'Loss')],color=['green', 'red'])
axis[0, 1].set_title("I 2022")


axis[0, 2].bar(['Profit', 'Loss'], [dataframe._get_value(1, 'Profit'), dataframe._get_value(1, 'Loss')], width=0.5,color=['green', 'red'])
axis[0, 2].set_title("II 2022")


axis[1, 0].bar(['Profit', 'Loss'], [dataframe._get_value(2, 'Profit'), dataframe._get_value(2, 'Loss')], width=0.5,color=['green', 'red'])
axis[1, 0].set_title("III 2022")


axis[1, 1].bar(['Profit', 'Loss'], [dataframe._get_value(3, 'Profit'), dataframe._get_value(3, 'Loss')], width=0.5,color=['green', 'red'])
axis[1, 1].set_title("IV 2022")

axis[1, 2].bar(['Profit', 'Loss'], [dataframe._get_value(4, 'Profit'), dataframe._get_value(4, 'Loss')], width=0.5,color=['green', 'red'])
axis[1, 2].set_title("V 2022")
plt.show()