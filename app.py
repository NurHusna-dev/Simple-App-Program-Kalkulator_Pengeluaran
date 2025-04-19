from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pendapatan  = float(request.form.get("pendapatan", 0))
        pengeluaran = {
            "makanan": float(request.form.get("makanan", 0)),
            "transportasi": float(request.form.get("transportasi", 0)),
            "utilitas": float(request.form.get("utilitas", 0)),
            "lainnya": float(request.form.get("lainnya", 0))
        }

        total_pengeluaran = sum(pengeluaran.values())
        sisa = pendapatan - total_pengeluaran
        persentase = (total_pengeluaran / pendapatan * 100) if pendapatan > 0 else 0

        return render_template("result.html",
                               pendapatan=pendapatan,
                               pengeluaran=pengeluaran,
                               total=total_pengeluaran,
                               sisa=sisa,
                               persen=persentase)
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run()