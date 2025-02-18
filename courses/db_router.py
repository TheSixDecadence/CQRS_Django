class CQRSRouter:
    def db_for_read(self, model, **hints):
        #Usar la base de datos de lectura para las consultas
        if model.__name__.endswith('Query'):
            return 'read_db'
        return None
    
    def db_for_write(self, model, **hints):
        #Usar la base de datos de escritura para las escrituras
        if model.__name__.endswith('Command'):
            return 'default'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        #Permitir relaciones si ambos objetos están en la misma base de datos
        return obj1._state.db == obj2._state.db
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        #Solo migrar la base de datos de escritura
        return db == 'default'