import csv

FICHIER_DONNEES = "data.csv"
FICHIER_RAPPORT = "rapport.txt"


def lire_donnees():
    eleves = []

    with open(FICHIER_DONNEES, newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)

        for ligne in lecteur:
            eleve = {
                "nom": ligne["nom"],
                "maths": int(ligne["maths"]),
                "nsi": int(ligne["nsi"]),
            }
            eleves.append(eleve)

    return eleves


def moyenne(liste):
    return sum(liste) / len(liste)


def analyser_resultats(eleves):
    maths = [e["maths"] for e in eleves]
    nsi = [e["nsi"] for e in eleves]

    moyenne_maths = moyenne(maths)
    moyenne_nsi = moyenne(nsi)

    moyennes_generales = []
    for e in eleves:
        moyenne_eleve = (e["maths"] + e["nsi"]) / 2
        moyennes_generales.append((e["nom"], moyenne_eleve))

    meilleur_eleve = max(moyennes_generales, key=lambda x: x[1])

    meilleure_matiere = "Maths" if moyenne_maths > moyenne_nsi else "NSI"

    return {
        "moyenne_maths": moyenne_maths,
        "moyenne_nsi": moyenne_nsi,
        "meilleur_eleve": meilleur_eleve,
        "meilleure_matiere": meilleure_matiere,
        "moyennes_generales": moyennes_generales,
    }


def generer_rapport(resultats):
    with open(FICHIER_RAPPORT, "w", encoding="utf-8") as fichier:

        fichier.write("RAPPORT D'ANALYSE DES RESULTATS\n")
        fichier.write("-" * 35 + "\n\n")

        fichier.write(f"Moyenne en Maths : {resultats['moyenne_maths']:.2f}\n")
        fichier.write(f"Moyenne en NSI   : {resultats['moyenne_nsi']:.2f}\n\n")

        fichier.write("Moyenne générale par élève :\n")
        for nom, moy in resultats["moyennes_generales"]:
            fichier.write(f"- {nom} : {moy:.2f}\n")

        fichier.write("\n")
        fichier.write(
            f"Meilleur élève : {resultats['meilleur_eleve'][0]} "
            f"({resultats['meilleur_eleve'][1]:.2f})\n"
        )
        fichier.write(f"Matière la plus réussie : {resultats['meilleure_matiere']}\n")
        fichier.close()


def main():
    eleves = lire_donnees()
    resultats = analyser_resultats(eleves)
    generer_rapport(resultats)
    print("Analyse terminée. Rapport généré dans rapport.txt")


if __name__ == "__main__":
    main()