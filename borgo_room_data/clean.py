import pandas as pd
import numpy as np
import csv
from dateutil import parser
from datetime import date, timedelta

# bookings = pd.read_csv('~/Desktop/final_project/borgo_room_data/bookings.csv')
# thirteen = pd.read_csv('~/Desktop/final_project/borgo_room_data/2013.csv')
# # fourteen = pd.read_csv('~/Desktop/final_project/borgo_room_data/2014.csv')


# print thirteen

# thirteen = thirteen.drop(['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], 1)
# thirteen = thirteen[thirteen.Date != 'xx-x']

# print len(thirteen)

# with open('2014_.csv', 'w') as f:
#     thirteen.to_csv(f, index=False)


data = []
with open('bookings_.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        row.append(i) # add an ID
        data.append(row)

headers = data[0]
# print headers[16] #14 and 15 are the dates
# print data[1][16]
data = data[1:]

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#separate into one entry for each day booked, instead of one entry for each date-range booked
new = []
for entry in data:
    start_date = parser.parse(entry[14], dayfirst=True)
    end_date = parser.parse(entry[15], dayfirst=True)
    if entry[12] == 'BCB' or entry[12] == 'BCM' or entry[12] == 'BCS':
        entry.append(2)
    elif entry[12] == 'BM' or entry[12] == 'BS':
        entry.append(4)
    elif entry[12] == 'LB' or entry[12] == 'LBW' or entry[12] == 'LM' or entry[12] == 'LS' or entry[12] == 'LSW' or entry[12] == 'EGN':
        entry.append(3)
    else:
        entry.append(1)
    i = 0
    for date in daterange(start_date, end_date):
        i += 1
    #check if start and end date are the same
    if start_date == end_date:
        new.append(entry[:15] + entry[16:])
    else:
        if entry[16] != '0':
            entry[16] = float(entry[16])/i
        for date in daterange(start_date, end_date):
            front = entry[:14]
            back = entry[16:]
            front.append(date.strftime('%d/%m/%Y'))
            front.extend(back)
            new.append(front)

# print new[48620:]

headers = ['DataPrenotazione', 'Pratica', 'CodMercato', 'Mercato',
           'CodSource', 'DesSource', 'CodMezzoComunicazione',
           'DesMezzoComunicazione', 'CodMotivo', 'DesMotivo',
           'codcam', 'GruppoTipologia', 'codtip', 'Tipologia',
           'date_res', 'RicaviRoom', 'RicaviTotali',
           'CodNaz', 'NazCli', 'CittaCliente', 'SessoCliente',
           'EtaCliente', 'CodAgenzia', 'Agenzia', 'CodDitta',
           'Ditta', 'Trattamento', 'Tariffa', 'CodOpportunit\x88',
           'DesOpportunita', 'res_id', 'room_type']

with open('bookings_final.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(headers)
    for row in new:
        writer.writerow(row)

