1. CoRE-MOF Data contains CoRE-MOF labels (geometric descriptors, chemistry RACs, MOF properties such as gas adsorption)
2. QMOF Data contains QMOF labels (band gap)
3. scripts folder contains code used to extract DOI, journal names, property compilation from the computational side. If you want to run the code yourself, drag them to the main directory and run it.
4. CoRE_QMOF_intersection_properties.csv is a CSV file that:
(a) has MOFs that intersect between CoRE-MOF and QMOF (N = 1164)
(b) Has its DOIs and journal name (taken from CCDC API)
(c) Has the computational labels from CoRE-MOF and QMOF mentioned previously

5. intersection_properties.csv is a CSV file that is essentially CoRE_QMOF_intersection_properties.csv but without DOI and journal name.
6. DOI_REF.pickle is a dictionary that maps DOI to CSD ref code taken from CCDC API (if you want to access this, unfortunately you'll need Python 3.9 and below, because of pickle's version). This dictionary is for the ENTIRE CSD dataset.
(a) Due to this, I created a text file (doi_to_journal.txt) that maps every single CSD entry's DOI to the journal name, so anyone with any Python version can access this.

If you have any questions, please ask me (Sartaaj Khan). Cheers.
