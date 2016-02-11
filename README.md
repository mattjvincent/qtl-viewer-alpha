For every dataset to be displayed...

/[dataset name]
      attribute (name='name of the experiment')

	/features			table of feature (gene, transcript, etc) ids (in our case ensembl ids), 
		
1: feature_id
		2: group_id
		3: chrom
		4: location (in Mb)
		5: name
		6: description

		* if genes, group_id = feature_id, 
		   if pQTL, the group_id will be gene_id while the feature_id will be protein id


	/markers			table of markers 

1: marker_id
2: chrom
3: location in (Mb)                                                    


	/lod
		/lod		table of lod scores, features (rows) x markers (columns)


# THIS (COEF, EFFECT PLOT)

	/coef 
		/strains		table of strains (cc founders), 1st col is unique identifier

			1: strain_id
			2: name
			3: description
	
		/coef		table of coef scores, features x strains x markers


# OR THIS (SAMPLES, FACT VIEWER)

	/samples			table of samples, 1st col is unique identifier

1: sample_id
2: name
3: description


	/phenotypes
		/factors		table of factors (sex, diet, tissue), 1st col is unique identifier

1: factor_id
2: name
3: description

		/phenotypes	table of phenotypes samples (rows) x factors (columns)


	/genotypes
		/genotypes	table of genotypes markers (rows) x samples (columns) 


	/expression
		/expression	table of expression values features (rows) x samples (columns)  



