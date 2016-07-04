Select * into new_carscoza_workings from newcars_carscoza;

delete from new_carscoza_workings where price is null;
