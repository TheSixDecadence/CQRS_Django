class CQRSRouter:
    def dbForRead(self, model, **hints):
        #Usar la base de datos de lectura para las consultas
        if model.__name__.endswith('Query'):
            return 'read_db'
        return None
    
    def dbForWrite(self, model, **hints):
        #Usar la base de datos de escritura para las escrituras
        if model.__name__.endswith('Command'):
            return 'write_db'
        return None
    
    def allowRelation(self, obj1, obj2, **hints):
        #Permitir relaciones si ambos objetos están en la misma base de datos
        return obj1._state.db == obj2._state.db
    
    def allowMigrate(self, db, app_label, model_name=None, **hints):
        #Solo migrar la base de datos de escritura
        return db == 'write_db'