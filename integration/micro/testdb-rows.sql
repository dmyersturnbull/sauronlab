/*
Sample Insertion SQL Queries to populate test db. Make sure unique keys are different for the VALUES.
*/

USE kaletest;
SET FOREIGN_KEY_CHECKS=1;


INSERT INTO refs (name,  description) VALUES ('manual', 'Manual');
INSERT INTO refs (name, description) VALUES ('manual:high', 'High-priority');
INSERT INTO refs (name, description) VALUES ('manual:johnson', 'User-added');

INSERT INTO suppliers (name, description) VALUES ('Amazon.com', 'Amazon.com');

INSERT INTO saurons (name) VALUES ('Elephant');
INSERT INTO saurons (name) VALUES ('Epsilon');

INSERT INTO users (username, first_name, last_name) VALUES ('johnson', 'Jackie', 'Johnson');
INSERT INTO users (username, first_name, last_name) VALUES ('annette', 'Annette', 'Antoinette');

INSERT INTO locations (name, part_of) VALUES ('Local Group', NULL);
INSERT INTO locations (name, part_of) VALUES ('Alpha Centauri', 1);
INSERT INTO locations (name, part_of) VALUES ('Isle of the Deep', 2);

INSERT INTO control_types(name, description, positive, genetics_related, drug_related) VALUES('neg', 'neg', 0, 0, 1);
INSERT INTO control_types(name, description, positive, genetics_related, drug_related) VALUES('pos', 'pos', 1, 0, 1);
INSERT INTO control_types(name, description, positive, genetics_related, drug_related) VALUES('gen-', 'gen-', 0, 1, 0);
INSERT INTO control_types(name, description, positive, genetics_related, drug_related) VALUES('gen+', 'gen+', 1, 1, 0);

INSERT INTO project_types(name, description) VALUES ('main', 'Main type of project');

INSERT INTO projects(name, description, creator_id) VALUES ('eat', 'Eating food', 1);

INSERT INTO stimuli(name, default_color, description, analog) VALUES ('spikes', '000000', 'Spikes, of course', 1);
INSERT INTO stimuli(name, default_color, description, analog) VALUES ('gaps', '000000', 'Things to jump over', 0);

INSERT INTO batteries(
    name, description, length, author_id, assays_sha1
) VALUES (
    'buffet', 'Buffet', 30, 1, unhex(repeat('a', 40))
);

INSERT INTO assays(
    name, description, length, frames_sha1
) VALUES (
    'pizza', 'This pizza has one topping and is longer', 2000, unhex(repeat('b', 40))
);
INSERT INTO assays(
    name, description, length, frames_sha1
) VALUES (
    'salad', 'This salad has two ingredients and is shorter', 1000, unhex(repeat('c', 40))
);

INSERT INTO stimulus_frames (assay_id, stimulus_id, frames, frames_sha1) VALUES (
    1, 1,
    X'00000000000000000000ffffffffffffffffffff0000000000000000000000000000000000000000ffffffffffffffffffff00000000000000000000',
    unhex(repeat('a', 40))
);

INSERT INTO stimulus_frames (
    assay_id, stimulus_id, frames, frames_sha1
) VALUES (
    2, 1,
    X'00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff',
    unhex(repeat('b', 40))
);
INSERT INTO stimulus_frames (
    assay_id, stimulus_id, frames, frames_sha1
) VALUES (
    2, 2,
    X'ffffffffffffffffffffffffffffff000000000000000000000000000000ffffffffffffffffffffffffffffff000000000000000000000000000000',
    unhex(repeat('c', 40))
);

INSERT INTO assay_positions (battery_id, assay_id, start) VALUES (1, 1, 0);
INSERT INTO assay_positions (battery_id, assay_id, start) VALUES (1, 2, 30);

INSERT INTO experiments(
    name, description, creator_id, project_id, battery_id, template_plate_id, default_acclimation_sec
) VALUES (
    'Eat', 'Eating a buffet', 1, 1, 1, NULL, 60
);


INSERT INTO sauron_configs (sauron_id, datetime_changed, description) VALUES (1, '2011-01-01 11:11:11', 'Nope');

INSERT INTO sauron_configs (sauron_id, datetime_changed, description) VALUES (2, '2011-01-01 11:11:11', 'Epsilon-ish');

INSERT INTO sauron_settings (sauron_config_id, name, value) VALUES (1, 'frames_per_second', 1);
-- no fps for Epsilon

INSERT INTO plate_types(name, n_rows, n_columns, well_shape, opacity) VALUES('2x3', 2, 3, 'square', 'opaque');

INSERT INTO plates(plate_type_id, person_plated_id, datetime_plated) VALUES(1, 1, '2021-01-01 09:09:09');

INSERT INTO plates(plate_type_id, person_plated_id, datetime_plated) VALUES(1, 1, '2021-02-02 09:09:09');

INSERT INTO submissions(
    lookup_hash, experiment_id, user_id, person_plated_id, continuing_id,
    datetime_plated, datetime_dosed, acclimation_sec, description
) VALUES (
    '111111111111', 1, 1, 1, NULL,
    '2021-01-01 09:09:09', '2021-01-01 10:10:10', 60, 'A submission of sorts'
);
INSERT INTO submissions(
    lookup_hash, experiment_id, user_id, person_plated_id, continuing_id,
    datetime_plated, datetime_dosed, acclimation_sec, description
) VALUES (
    '222222222222', 1, 1, 1, NULL,
    '2021-02-02 09:09:09', '2021-02-02 10:10:10', 60, 'A 2nd submission of sorts'
);
INSERT INTO submissions(
    lookup_hash, experiment_id, user_id, person_plated_id, continuing_id,
    datetime_plated, datetime_dosed, acclimation_sec, description
) VALUES (
    '333333333333', 1, 1, 1, NULL,
    '2021-03-03 09:09:09', '2021-03-03 10:10:10', 60, 'A 3rd submission of sorts'
);

INSERT INTO runs(
    experiment_id, plate_id, description, experimentalist_id, submission_id, datetime_run, datetime_dosed,
    name, tag, sauron_config_id, config_file_id, incubation_min, acclimation_sec
) VALUES (
    1, 1, 'Plate 1, run 1', 1, 1, '2012-01-01 11:11:11', '2012-01-01 10:10:10',
    'run:1', '20120101.11111111.Elephant', 1, NULL, 61, 60
);

INSERT INTO runs(
    experiment_id, plate_id, description, experimentalist_id, submission_id, datetime_run, datetime_dosed,
    name, tag, sauron_config_id, config_file_id, incubation_min, acclimation_sec
) VALUES (
    1, 1, 'Plate 1, run 2', 1, 2, '2012-01-01 12:12:12', '2012-01-01 10:10:10',
    'run:2', '20120101.121212.Elephant', 1, NULL, 61, 60
);

INSERT INTO runs(
    experiment_id, plate_id, description, experimentalist_id, submission_id, datetime_run, datetime_dosed,
    name, tag, sauron_config_id, config_file_id, incubation_min, acclimation_sec
) VALUES (
    1, 2, 'Plate 2, run 1', 1, 3, '2012-01-01 12:12:12', '2012-01-01 10:10:10',
    'run:3', '20120101.121212.Epsilon', 2, NULL, 61, 60
);


INSERT INTO genetic_variants(name, creator_id) VALUES('A genetic superbreed', 1);
INSERT INTO genetic_variants(name, creator_id) VALUES('A 2nd genetic superbreed', 1);

INSERT INTO compounds(
    inchi, inchikey, inchikey_connectivity, chembl_id, chemspider_id, smiles
) VALUES (
    'InChI=1S/H2O/h1H2', 'XLYOFNOQVPJJNP-UHFFFAOYSA-N', 'XLYOFNOQVPJJNP', 'CHEMBL1098659', 937, 'O'
);
INSERT INTO compounds(
    inchi, inchikey, inchikey_connectivity, chembl_id, chemspider_id, smiles
) VALUES (
    'InChI=1S/C2H6OS/c1-4(2)3/h1-2H3', 'IAZDPXIOMUYVGZ-UHFFFAOYSA-N', 'IAZDPXIOMUYVGZ', 'CHEMBL504', 659, 'CS(=O)C'
);
INSERT INTO compounds(
    inchi, inchikey, inchikey_connectivity, chembl_id, chemspider_id, smiles
) VALUES (
    'InChI=1S/CH4O/c1-2/h2H,1H3', 'OKKJLVBELUTLKV-UHFFFAOYSA-N', 'OKKJLVBELUTLKV', 'CHEMBL14688', 864, 'CO'
);
INSERT INTO compounds(
    inchi, inchikey, inchikey_connectivity, chembl_id, chemspider_id, smiles
) VALUES (
    'InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3', 'LFQSCWFLJHTTHZ-UHFFFAOYSA-N', 'LFQSCWFLJHTTHZ', 'CHEMBL545', 682, 'CCO'
);
-- fluoxetine HCl
INSERT INTO compounds(
    inchi, inchikey, inchikey_connectivity, chembl_id, chemspider_id, smiles
) VALUES (
    'InChI=1S/C17H18F3NO/c1-21-12-11-16(13-5-3-2-4-6-13)22-15-9-7-14(8-10-15)17(18,19)20/h2-10,16,21H,11-12H2,1H3',
    'RTHCYVBBDHJXIQ-UHFFFAOYSA-N', 'RTHCYVBBDHJXIQ', 'CHEMBL41', 3269, 'C(c1ccc(OC(c2ccccc2)CCNC)cc1)(F)(F)F'
);
-- cocaine
INSERT INTO compounds(
    inchi, inchikey, inchikey_connectivity, chembl_id, chemspider_id, smiles
) VALUES (
    'InChI=1S/C17H21NO4/c1-18-12-8-9-13(18)15(17(20)21-2)14(10-12)22-16(19)11-6-4-3-5-7-11/h3-7,12-15H,8-10H2,1-2H3/t12-,13+,14-,15+/m0/s1',
    'ZPUCINDJVBIVPJ-LJISPDSOSA-N', 'ZPUCINDJVBIVPJ', 'CHEMBL370805', 10194104, 'CN1[C@H]2CC[C@@H]1[C@H]([C@H](C2)OC(=O)c3ccccc3)C(=O)OC'
);

INSERT INTO batches(
    lookup_hash, tag, compound_id, ref_id, supplier_id, molecular_weight
) VALUES (
    'water000000000', 'water', 1, 1, 1, 18.01528
);
INSERT INTO batches(
    lookup_hash, tag, compound_id, ref_id, supplier_id, molecular_weight
) VALUES (
    'dmso0000000000', 'DMSO', 2, 1, 1, 78.13
);
INSERT INTO batches(
    lookup_hash, tag, compound_id, ref_id, supplier_id, molecular_weight
) VALUES (
    'meoh0000000000', 'methanol', 3, 1, 1, 32.04
);
INSERT INTO batches(
    lookup_hash, tag, compound_id, ref_id, supplier_id, molecular_weight
) VALUES (
    'etoh0000000000', 'ethanol', 4, 1, 1, 46.07
);

INSERT INTO batches(
    lookup_hash, tag, compound_id, made_from_id, supplier_id, ref_id,
    legacy_internal_id, location_id, box_number, well_number, location_note,
    amount, concentration_millimolar, solvent_id, molecular_weight, supplier_catalog_number,
    person_ordered, date_ordered
) VALUES (
    'fluoxetine.100', 'fluoxetine', 5, NULL, 1, 1,
    'legacy-flu-100', 1, 1, 1, NULL,
    '10 g', 100, 2, 345.8, 'flu.id1', 1, '2009-06-01 10:10:10'
);

INSERT INTO batches(
    lookup_hash, tag, compound_id, made_from_id, supplier_id, ref_id,
    legacy_internal_id, location_id, box_number, well_number, location_note,
    amount, concentration_millimolar, solvent_id, molecular_weight, supplier_catalog_number,
    person_ordered, date_ordered
) VALUES (
    '0fluoxetine.30', NULL, 5, 5, 1, 1,
    'legacy-flu-30', 1, 1, 2, NULL,
    '1 uL', 30, 2, 345.8, 'flu.id1', 1, '2009-11-01 11:11:11'
);

INSERT INTO batches(
    lookup_hash, tag, compound_id, made_from_id, supplier_id, ref_id,
    legacy_internal_id, location_id, box_number, well_number, location_note,
    amount, concentration_millimolar, solvent_id, molecular_weight, supplier_catalog_number,
    person_ordered, date_ordered
) VALUES (
    '0000cocaine.10', NULL, 6, NULL, 1, 1,
    'legacy-flu-30', 1, 2, 1, NULL,
    '1 mg', 10, 2, 345.8, 'flu.id1', 1, '2008-11-01 09:09:09'
);

-- drug (-) control
INSERT INTO wells(
    run_id, well_index, control_type_id, variant_id, well_group, n, age
) VALUES (
    1, 1, 1, 1, NULL, 10, 7
);
-- drug (+) control, with drug
INSERT INTO wells(
    run_id, well_index, control_type_id, variant_id, well_group, n, age
) VALUES (
    1, 2, 2, 1, NULL, 10, 7
);
-- different variant
INSERT INTO wells(
    run_id, well_index, control_type_id, variant_id, well_group, n, age
) VALUES (
    1, 3, NULL, 2, NULL, 10, 7
);
-- single compound treatment
INSERT INTO wells(
    run_id, well_index, control_type_id, variant_id, well_group, n, age
) VALUES (
    1, 4, NULL, 1, NULL, 10, 7
);
-- co-treatment, one without a compounds row
INSERT INTO wells(
    run_id, well_index, control_type_id, variant_id, well_group, n, age
) VALUES (
    1, 5, NULL, 1, NULL, 10, 7
);
-- new well group
INSERT INTO wells(
    run_id, well_index, control_type_id, variant_id, well_group, n, age
) VALUES (
    1, 6, NULL, 1, 'a well group', 10, 7
);

INSERT INTO well_treatments(well_id, batch_id, micromolar_dose) VALUES (1, 1, 50.0);
INSERT INTO well_treatments(well_id, batch_id, micromolar_dose) VALUES (2, 1, 50.0);
INSERT INTO well_treatments(well_id, batch_id, micromolar_dose) VALUES (2, 2, 25.0);

INSERT INTO features (
    id, name, description, dimensions, data_type
) VALUES (
    1, 'MI', 'motion index', '[t-1]', 'float'
);
INSERT INTO features (
    id, name, description, dimensions, data_type
) VALUES (
    2, 'cd(10)', 'cd(10)', '[t-1]', 'float'
);
