"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Optional, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name", validators=[DataRequired()])
    description = StringField("Description", validators=[
                              Optional(), Length(max=2000)])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title", validators=[
                        DataRequired(), Length(max=255)])
    artist = StringField("Artist", validators=[
                         DataRequired(), Length(max=255)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
