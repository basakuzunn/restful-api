from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import logging
from datetime import datetime



app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


logging.basicConfig(filename="std.log",
                    format=' {%(message)s} , {%(asctime)s}',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable= False)
    views = db.Column(db.Integer, nullable= False)
    likes = db.Column(db.Integer, nullable= False)

    def __repr__(self):
        return "Video(name = {name},views = {views}, likes = {likes})"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes of the video")

video_del_args = reqparse.RequestParser()
video_del_args.add_argument("name", type=str, help="Name of the video is required")
video_del_args.add_argument("views", type=int, help="Views of the video")
video_del_args.add_argument("likes", type=int, help="Likes of the video")

resource_fields = {
    'id' : fields.Integer,
    'name': fields.String,
    'views':fields.Integer,
    'likes':fields.Integer
}
def time(filename, count):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)

    file = open(filename, "a")
    line = file.write(str(count) + ',' + str(current_time)+'\n')
    file.close()


count_get = 0
count_put = 0
count_patch = 0
count_del = 0


class Video(Resource):
    def __init__(self):
        self.count_get = 0
    @marshal_with(resource_fields)
    def get(self,video_id):
        time("getfile.txt",self.count_get)
        self.count_get +=1
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,message="Could not find video with that id")
        return result

    def __init__(self):
        self.count_put = 0
    @marshal_with(resource_fields)
    def put(self,video_id):
        time("putfile.txt", self.count_put)
        self.count_put += 1
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message= "Video id taken...")
        video = VideoModel(id=video_id, name=args['name'], views = args['views'], likes =args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201


    def __init__(self):
        self.count_patch = 0
    @marshal_with(resource_fields)
    def patch(self, video_id):
        time("patchfile.txt", self.count_patch)
        self.count_patch += 1
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message= "Video does not exist, cannot update")

        if args['name']:
           result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']


        db.session.commit()

        return result



    def __init__(self):
        self.count_del = 0
    @marshal_with(resource_fields)
    def delete(self, video_id):
        time("delfile.txt", self.count_del)
        self.count_del += 1
        args = video_del_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(204, message="Video is deleted.")
        if not result:
            abort(404, message="Video does not exist, cannot delete.")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])

        db.session.delete(video)
        db.session.commit()
        return video, 204

api.add_resource(Video,"/video/<int:video_id>")
if __name__ == "__main__":
    app.run(debug=True)