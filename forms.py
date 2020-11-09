"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Playlist Name', validators=[InputRequired(message="Enter the playlist name")])
    description = TextAreaField('Playlist Description')


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[InputRequired(message="Enter the song title")])
    artist = StringField('Artist', validators=[InputRequired(message="Enter the artist")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
