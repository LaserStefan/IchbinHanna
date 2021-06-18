import matplotlib.pyplot as plt

labels = 'German', 'English', 'Others (all below < 1%)'
sizes = [83, 11, 6]
explode = (0.1, 0, 0)  # only "explode" the 1ST slice

fig1, ax1 = plt.subplots()

ax1.pie(sizes, explode=explode, labels=labels, colors= ['#756bb1', '#bcbddc', '#efedf5'], autopct='%1.0f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title("Language of all #IchbinHanna Tweets")
plt.savefig('../pie_users.png', dpi=300)
plt.show()
