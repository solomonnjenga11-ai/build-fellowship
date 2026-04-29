def llm_decision(regime, ml_prob, sma_signal, volatility, macro):
    """
    Combine all signals into a simple rule-based decision.
    This is your LLM placeholder for the MVP.
    """

    # 1. Macro sentiment influence
    macro_bias = 0
    if macro.get("rate_stance") == "hawkish":
        macro_bias += 1
    if macro.get("rate_stance") == "dovish":
        macro_bias -= 1
    if macro.get("employment") == "strong":
        macro_bias += 1
    if macro.get("employment") == "weak":
        macro_bias -= 1

    # 2. ML probability influence
    if ml_prob > 0.6:
        ml_signal = 1
    elif ml_prob > 0.5:
        ml_signal = 0.5
    else:
        ml_signal = 0

    # 3. Regime influence
    if regime == "shock":
        regime_penalty = -1
    elif regime == "normal":
        regime_penalty = 0
    else:  # calm
        regime_penalty = 0.5

    # 4. Combine everything
    score = ml_signal + macro_bias + regime_penalty

    # 5. SMA/ATR direction filter
    if sma_signal == "long":
        score += 0.5
    elif sma_signal == "short":
        score -= 0.5

    # 6. Volatility filter
    if volatility > 0.02:
        score -= 0.5

    # 7. Final decision
    if score >= 1.5:
        return "TRADE"
    elif score >= 0.5:
        return "REDUCE"
    else:
        return "AVOID"
