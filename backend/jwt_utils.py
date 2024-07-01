from flask_jwt_extended import JWTManager

# 初始化JWT
jwt = JWTManager()

# 定义撤销令牌列表（仅示例，实际应存储在数据库或缓存中）
revoked_tokens = set()

# 在验证JWT时检查令牌是否已撤销的函数
@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_data):
    jti = jwt_data['jti']
    return jti in revoked_tokens
def init_jwt(app):
    jwt.init_app(app)
