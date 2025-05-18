import streamlit as st
import google.auth as ga
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Magic constants here
sheet_id = "1rs37GT6bir0W5Qs9Wqd51Dd5ZJlulnTGmTGfUk5RzfA"

mood_send = ""


# goog api sender
def append_values(spreadsheet_id, range_name, value_input_option, _values):
# def send_data(mood):
    creds, _ = ga.default()
    try:
        service = build("sheets", "v4", credentials=creds)

        values = [
            [
                # Cell values ...
            ],
            # Additional rows ...
        ]
        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .append(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute()
        )
        print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
        return result

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


# st page below

st.title("Placeholder title")

st.markdown("Placeholder text")

if st.button("button1"):
    mood_send = "happy"

if st.button("button2"):
    mood_send = "sad"

if st.button("submit button"):
    st.write("sending thing")
    st.write(mood_send)
    append_values(
      sheet_id,
      "A1:C2",
      "USER_ENTERED",
      [["F", "B"], ["C", "D"]],
  )

