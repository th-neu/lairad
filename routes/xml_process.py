"""
process the xml response and add it to the database
"""
import xml.etree.ElementTree as ET
from db import get_db


def process_xml_response(xml_response):
    """process xml and write to db"""
    root = ET.fromstring(xml_response)
    thought_text = root.find("thoughts/text").text
    reasoning_text = root.find("thoughts/reasoning").text
    plan_text = root.find("thoughts/plan").text
    criticism_text = root.find("thoughts/criticism").text
    command_name = root.find("command/name").text
    arg_value = root.find("command/args/arg_value").text

    # Store the extracted data in the database
    conn = get_db()
    c = conn.cursor()

    # Store thought text
    c.execute('INSERT INTO thoughts (thought_text, reasoning_text, plan, criticism, command, command_args) VALUES (?, ?, ?, ?, ?, ?)', (thought_text, reasoning_text, plan_text, criticism_text, command_name, arg_value))

    conn.commit()
    conn.close()
