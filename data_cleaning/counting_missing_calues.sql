SELECT 
    COUNT(CASE WHEN "Total Population" = '-' THEN 1 END) AS missing_total_population,
    COUNT(CASE WHEN "Urban Population" = '-' THEN 1 END) AS missing_urban_population,
    COUNT(CASE WHEN "Rural Population" = '-' THEN 1 END) AS missing_rural_population,
    COUNT(CASE WHEN "Population Density" = '-' THEN 1 END) AS missing_population_density,
    COUNT(CASE WHEN "Life Expectancy" = '-' THEN 1 END) AS missing_life_expectancy,
    COUNT(CASE WHEN "Birth Rate" = '-' THEN 1 END) AS missing_birth_rate,
    COUNT(CASE WHEN "Death Rate" = '-' THEN 1 END) AS missing_death_rate,
    COUNT(CASE WHEN "Fertility Rate" = '-' THEN 1 END) AS missing_fertility_rate,
    COUNT(CASE WHEN "Infant Mortality Rate" = '-' THEN 1 END) AS missing_infant_mortality_rate,
    COUNT(CASE WHEN "Growth Rate" = '-' THEN 1 END) AS missing_growth_rate
FROM pop;
