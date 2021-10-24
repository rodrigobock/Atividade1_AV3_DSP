from config import *

class Carro(db.Model):
    # atributos do carro
    id = db.Column(db.Integer, primary_key=True)
    Modelo = db.Column(db.String(254))
    Marca = db.Column(db.String(254))
    QtdePortas = db.Column(db.String(254))
    Motor = db.Column(db.String(254))

    # método para expressar os carros em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.Modelo + ", " + self.Marca + ", " + self.QtdePortas + ", " + self.Motor
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "Modelo": self.Modelo,
            "Marca": self.Marca,
            "QtdePortas": self.QtdePortas,
            "Motor": self.Motor
        }
 
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()


    c1 = Carro(Modelo = "Clio", Marca = "Renault", QtdePortas = "4", Motor = "1.0") 
    c2 = Carro(Modelo = "Sandero", Marca = "Renault", QtdePortas = "4", Motor = "1.0") 
    c3 = Carro(Modelo = "Palio", Marca = "Fiat", QtdePortas = "2", Motor = "1.0") 

    db.session.add(c1)
    db.session.add(c2)
    db.session.add(c3)
    db.session.commit()