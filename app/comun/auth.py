#cuando algien inicie secion (lo programa E1), se guardan SIEMPRE estas 3 llaves:
#   SESSION["usuario_id"] -> int (usuario.usuario_id)
#   session["rol"]        -> str (exactamente uno de roles, igual que rol.nombre en la BD)
#   session["nombre"]     -> str (para mostrar en el encabezado )

from functools import wraps

from flask import abort, flash, redirect, session, url_for

ROLES =("Administrador", "Orientadora", "Alumno", "Pabre de familia")

def login_requerido(vista):
    """ La ruta solo se abre si hay una sesion iniciada. """

    @wraps(vista)
    def envoltura(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Indice sesion para continuar.", "info")
            return redirect(url_for("login.entrar"))
        return vista(*args, **kwargs)
    return envoltura

def rol_requerido(*roles_permitidos):
    """La ruta solo se abre si el rol de la sesion esta en la lista."""
    for rol in roles_permitidos:
        if rol not in ROLES:
            raise ValueError(f"Rol desconocido un @rol_requerido: {rol!r}")

    def decorador(vista):
        @wraps(vista)
        @login_requerido
        def envoltura(*args, **kwargs):
            if session.get("rol") not in roles_permitidos:
                abort(403)
            return vista(*args, **kwargs)
        return envoltura
    return decorador