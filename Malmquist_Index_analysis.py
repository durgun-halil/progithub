import numpy as np

data = {
    'Countries': ['USA', 'Türkiye', 'China', 'Canada', 'Japan', 'United Kingdom', 'France', 'Germany', 'Indonesia', 'India', 'Argentina', 'Australia', 'Italy', 'Brazil', 'Mexico', 'Saudi Arabia', 'Russia', 'South Africa', 'South Korea'],
    'Population': [328329953, 83481684, 141000000, 37601230, 126933000, 66836327, 67388001, 83092962, 269582878, 1038000000, 44938712, 25340297, 59729081, 211782878, 125085311, 35827362, 144406261, 58087055, 51000000],
    'Travel and Tourism Revenue': [2.39E+11, 4.14E+11, 3.58E+11, 23889000, 4.92E+11, 5.27E+11, 2.11E+11, 5.84E+11, 1.84E+11, 3.17E+11, 5.65E+11, 4.80E+11, 49530000000, 7.40E+11, 2.59E+11, 1.99E+11, 1.72E+11, 1.65E+11, 3.28E+10],
    'Number of Passengers': [926737000, 111131000, 659629000, 93352000, 130233000, 142392000, 71289000, 237200000, 116740000, 167499000, 19461000, 76850000, 190000000, 123000000, 69937000, 46181000, 108857000, 26211000, 1193000000],
    'Number of Flights': [10083000, 1556417, 5521000, 4740000, 1123607, 2254000, 2480000, 2100000, 956220, 2457500, 336100, 839870, 2730000, 951000, 875000, 912810, 1831190, 456911, 1210000],
    'Exchange Rate': [1, 5.67, 6.91, 1.33, 109.01, 0.78, 0.89, 0.8904, 1414767, 70.42, 48.15, 1.44, 0.89, 3.94, 19.26, 3.75, 64.03, 14.45, 1171.89],
    'Total Cargo Movements': [42498000, 6816000, 25395000, 3109000, 8919000, 5851000, 4523000, 7764000, 982000, 1938000, 280000, 1931000, 1345000, 1521000, 1073000, 2043000, 6481000, 450000, 5830000],
    'Number of Airports': [5080, 56, 238, 528, 98, 145, 464, 539, 237, 449, 1169, 561, 136, 737, 98, 232, 2418, 135, 119]
}


def malmquist_index(data):
    # Giriş ve çıktı verilerini al
    inputs_data = np.array([data['Population'], data['Number of Flights'], data['Exchange Rate'], data['Number of Airports']])
    output_data = np.array(data['Population'])
    
    # Normalize edilen verileri saklamak için matris oluştur
    normalized_data = np.zeros_like(inputs_data)
    
    # Giriş verilerini normalize et
    for i in range(inputs_data.shape[0]):
        max_val = np.max(inputs_data[i])
        min_val = np.min(inputs_data[i])
        normalized_data[i] = (inputs_data[i] - min_val) / (max_val - min_val)
    
    # İki zaman dönemi arasındaki Malmquist Endeksi'ni hesapla
    malmquist_scores = []
    for i in range(inputs_data.shape[1]):
        x0 = normalized_data[:, i]
        y0 = output_data[i]
        x1 = normalized_data[:, (i + 1) % inputs_data.shape[1]]
        y1 = output_data[(i + 1) % inputs_data.shape[1]]
        
        productivity_score = (y1 / y0) * np.prod(np.power(x1 / x0, 1 / inputs_data.shape[0]))
        malmquist_scores.append(productivity_score)
    
    return malmquist_scores

# Malmquist indeksi analizini yapma
malmquist_scores = malmquist_index(data)

# Sonuçları görüntüleme
for country, score in zip(data['Countries'], malmquist_scores):
    print(country, score)
