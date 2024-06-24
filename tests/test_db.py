import epiworldpy as epiworld

def test_db_simple():
    DAYS = 100

    covid19 = epiworld.ModelSEIR(
        name              = 'covid-19',
        n                 = 10000,
        prevalence        = .01,
        contact_rate      = 2.0,
        transmission_rate = .1,
        incubation_days   = 7.0,
        recovery_rate     = 0.14
    )

    covid19.run(DAYS, 223)

    history = covid19.getDb().getHistTotal()
    dates = history['dates']
    states = history['states']
    counts = history['counts']

    # Considering that the SEIR model has four states (susceptible, exposed, infected, and
    # recovered), we expect DAYS + 1 * 4 (we do the plus one since the resulting time series
    # starts at 0 and the upper bound is treated as inclusive by epiworld).
    EXPECTED_ENTRIES = (DAYS + 1) * 4

    assert len(dates) == EXPECTED_ENTRIES
    assert len(states) == EXPECTED_ENTRIES
    assert len(counts) == EXPECTED_ENTRIES