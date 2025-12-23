def analyze_risk(open_ports):
    high_risk_ports = {21, 22, 3306, 3389, 5432, 27017}
    medium_risk_ports = {80}

    if any(port in high_risk_ports for port in open_ports):
        return "HIGH", "🔴 High-risk services exposed"

    if any(port in medium_risk_ports for port in open_ports):
        return "MEDIUM", "🟡 Web service exposed (HTTP)"

    if 443 in open_ports:
        return "LOW", "🟢 Secure HTTPS service detected"

    return "LOW", "🟢 No common risky ports detected"
