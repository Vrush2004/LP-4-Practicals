# Write a program for Log Capturing and Event Correlation

import logging
import time
import random
from collections import defaultdict

# Configure the logging module
logging.basicConfig(filename='system_logs.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example log sources
log_sources = ['System', 'Application', 'Security']

# Event correlation criteria (example)
correlation_criteria = {
    'System Error': ['ERROR', 'CRITICAL'],
    'User Login Attempt': ['INFO', 'WARNING']
}

# Dictionary to store captured logs
captured_logs = defaultdict(list)

def log_event(source, level, message):
    """Log an event with a specified source, level, and message."""
    if level not in ['INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        print("Invalid log level.")
        return

    # Log the event
    logging.log(getattr(logging, level), f"{source}: {message}")
    captured_logs[source].append((level, message))

def correlate_events():
    """Correlate events based on predefined criteria."""
    correlated_events = defaultdict(list)
    
    for source, logs in captured_logs.items():
        for level, message in logs:
            for event_name, criteria in correlation_criteria.items():
                if level in criteria:
                    correlated_events[event_name].append((source, level, message))
    
    return correlated_events

def main():
    """Main function to simulate log capturing and event correlation."""
    # Simulate logging events from different sources
    for _ in range(10):
        source = random.choice(log_sources)
        level = random.choice(['INFO', 'WARNING', 'ERROR', 'CRITICAL'])
        message = f"This is a {level.lower()} message from {source}."
        
        log_event(source, level, message)
        time.sleep(1)

    # Correlate captured events
    correlated = correlate_events()
    
    # Display correlated events
    print("\nCorrelated Events:")
    for event_name, events in correlated.items():
        print(f"{event_name}:")
        for source, level, message in events:
            print(f"  Source: {source}, Level: {level}, Message: {message}")

if __name__ == "__main__":
    main()