from kellet_calc import daumann_kalk

taulengde=20 # meter
dybde=10 # meter
daumannsvekt=10 # kg
for daumannlengde in (10, 19):
    print()
    print("Putter ut %i meter med tau til daumann" % daumannlengde)
    ## hvor dypt vil daumannen befinne seg dersom tauet er helt stramt?
    expected_y_pos = dybde/taulengde*(taulengde-daumannlengde)
    ## max_dausynk - når tauet henger rett ned fra baugen, eller når daumann har truffet sjøbunnen
    max_dausynk = min(daumannlengde-(dybde-expected_y_pos), expected_y_pos)
    for dausynk in (0.01, 0.1, 0.5*max_dausynk, max_dausynk-0.01):
        results = daumann_kalk(daumannsvekt, taulengde, dybde, daumannlengde, dausynk)
        print("=====")
        print("Dausynk: %.2f m" % results['dausynk'])
        print("Vindkraft på båten: g * %.2f kg" % results['Bx'])
        print("Vinkel på ankerkraft (y:l - bør være mindre enn 1:3): 1:%.2f" % (results['l1']/results['l1y']))
        
