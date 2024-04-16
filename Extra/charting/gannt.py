import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
from datetime import datetime, timedelta
import pandas as pd


data = [
    ("Aanmaak en overleg groep", "2023-12-05", "2023-12-05", "Ja", 2),
    ("Overleg groep en vergadering", "2023-12-12", "2023-12-12", "Ja", 2),
    ("Ontwerp en keuze thema", "2023-12-13", "2023-12-13", "Ja*", 2),
    ("Vergadering over PVA", "2023-12-18", "2023-12-18", "Ja", 2),
    ("Opdracht 1 afgerond", "2023-12-20", "2023-12-20", "Ja", 1),
    ("PVA formaat maken", "2023-12-22", "2023-12-22", "Ja", 0.5),
    ("Vergadering over Gantt-chart", "2024-01-18", "2024-01-18", "Ja", 1),
    ("Website ontwikkeling", "2024-01-19", "2024-01-19", "Nee", 4),
    ("HTML afronding en overleg", "2024-01-20", "2024-01-20", "Ja", 4),
    ("Overleg met Mitch", "2024-01-21", "2024-01-21", "Nee", 3),
    ("Samenwerken aan website en Gantt", "2024-01-22", "2024-01-22", "Nee", 1.5),
    ("Requirements en feedback", "2024-01-24", "2024-01-24", "Ja", 3),
    ("Handleidingen en verantwoording", "2024-01-24", "2024-01-24", "Ja", 2.5),
    ("Afronden groepswebsite", "2024-01-24", "2024-01-25", "Nee", 4),
    ("Correcties en inleveren", "2024-01-26", "2024-01-26", "Ja", 5),
]

tasks = [{
    'Task': row[0],
    'Start': datetime.strptime(row[1], '%Y-%m-%d'),
    'Finish': datetime.strptime(row[1], '%Y-%m-%d') + timedelta(hours=row[4]),
    'Resource': row[3],
    'Hours': row[4]
} for row in data]

df = pd.DataFrame(tasks)

color_map = {'Ja': 'tab:green', 'Nee': 'tab:red', 'Ja*': 'tab:orange'}

fig, ax = plt.subplots(figsize=(10, 8))

for i, task in df.iterrows():
    start = mdates.date2num(task['Start'])
    finish = mdates.date2num(task['Finish'])
    ax.barh(task['Task'], finish - start, left=start, height=0.4,
            color=color_map[task['Resource']], align='center')

ax.xaxis_date()
date_format = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)

fig.autofmt_xdate()

ax.set_xlabel('Datum')
ax.set_ylabel('Activiteit')
ax.set_title('Gantt Chart van Projectactiviteiten')

for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

ax.xaxis.grid(True, which='major', linestyle='-')
ax.yaxis.grid(True, which='major', linestyle='-')


handles = [mpatches.Patch(color=color, label=label) for label, color in color_map.items()]
ax.legend(handles=handles, loc='lower right')

plt.show()
