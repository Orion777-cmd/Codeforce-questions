planned_rides, m_ride, ride_cost, m_cost = map(int, input().split())

if m_ride * ride_cost <= m_cost:
    print(planned_rides * ride_cost)
else:
    ans = (planned_rides // m_ride) * m_cost
    if (planned_rides % m_ride) * ride_cost <= m_cost:
        ans += (planned_rides % m_ride) * ride_cost
    else:
        ans += m_cost
    print(ans)
    