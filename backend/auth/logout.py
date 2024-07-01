from flask import request, jsonify, session
from auth import auth
from flask_jwt_extended import JWTManager, jwt_required,get_jwt
from database import db
from jwt_utils import  revoked_tokens
# 注销路由示例
@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # 从当前会话中删除用户信息
    session.pop('user', None)
    # 将当前令牌加入到撤销令牌列表中
    jti = get_jwt()['jti']
    revoked_tokens.add(jti)
    return jsonify({'message': 'Logout successful'}), 200
