from kellet_calc import daumann_kalk
from math import sqrt

dybde=10 # meter
daumannsvekt=10 # kg

for taulengde, daumannslengder in (
        (20, (10,19)),
        (25, (12.5,24)),
        (30, (1,15,25,29)),
        (40, (20,39))):
    print()
    print("=========================")
    print("legger ut %i meter med ankertau" % taulengde)
    print("=========================")
    for daumannlengde in daumannslengder:
        print("Putter ut %i meter med tau til daumann" % daumannlengde)
        ## hvor dypt vil daumannen befinne seg dersom tauet er helt stramt?
        expected_y_pos = dybde/taulengde*(taulengde-daumannlengde)
        ## max_dausynk - når tauet henger rett ned fra baugen, eller når daumann har truffet sjøbunnen
        max_dausynk = min(daumannlengde-(dybde-expected_y_pos), expected_y_pos)
        results = daumann_kalk(daumannsvekt, taulengde, dybde, daumannlengde, 0.0001)
        max_avstand = sqrt(taulengde**2-dybde**2)
        for dausynk in (0.01, 0.1, 0.5*max_dausynk, max_dausynk-0.01):
            results = daumann_kalk(daumannsvekt, taulengde, dybde, daumannlengde, dausynk)
            avstand = results['l1x']+results['l2x']
            print("=====")
            print("Dausynk: %.2f m" % results['dausynk'])
            print("Vindkraft på båten: g * %.2f kg" % results['Bx'])
            print("Vinkel på ankerkraft (y:l - bør være mindre enn 1:3): 1:%.2f" % (results['l1']/results['l1y']))
            print("Båtens avstand fra ankerpunkt: %.2f meter" % avstand)
            print("Delta avstand: %.2f meter" % (max_avstand-avstand))
        print()
        
