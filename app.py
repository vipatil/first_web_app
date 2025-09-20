from flask  import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    path = 'static/assets/paintings/'
    paintings = [
        {
            'title': 'Starry Night',
            'artist': 'Vincent van Gogh',
            'year': 1889,
            'image_url': path +'Vijay_P_BerryFarm_Oil_on_Panel_12x16_$500.JPG'
        },
        {
            'title': 'Mona Lisa',
            'artist': 'Leonardo da Vinci',
            'year': 1503,
            'image_url': path +'Vijay_P_FallSeason_Oil_On_Canvas_11x14_$500.jpg'
        },
        {
            'title': 'The Persistence of Memory',
            'artist': 'Salvador Dalí',
            'year': 1931,
            'image_url': path +'Vijay_P_KelonaLakeView_Oil_on_Panel_11x14_$500.jpg'
        }
    ]
    return render_template('index.html', paintings=paintings)

if __name__=="__main__":
    app.run(debug=True)