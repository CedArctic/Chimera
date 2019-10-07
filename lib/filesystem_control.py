
from lib.memory_management import memory
from pathlib import Path

class FileSystemControl:
    
    _CURRENT_PATH = '_current_path'
    
    _current_path = ""
    
    def __init__(self,initial_path=None):
        
        if initial_path:
            path = Path(initial_path)
        else:
            path = Path.cwd()
        
        path = self._check_path(path)
             
        self._current_path = path
    
    def _check_path(self,path):
        
        path = path.resolve()
        
        if not path.exists():
            raise Exception('Path [{}] does not exists!'.format(path))
        
        return path
    
    @memory
    async def load_path_from_memory(self,memory):
        memory_path = await memory.get(self._CURRENT_PATH)
        if memory_path:
            self._current_path = memory_path
    
    @memory
    async def set_path(self, path, relative=False,memory=None):
        new_path = Path(path) if not relative else Path(str(self._current_path),path)
        new_path = self._check_path(new_path)
        await memory.set(self._CURRENT_PATH,new_path)
        return new_path
    
    async def list_directory(self):
        dir_path = self._current_path
        if not dir_path.is_dir():
            dir_path = Path(*dir_path.parts[:-1])
        
        return [x for x in self._current_path.iterdir()]
        
    
    async def retrieve_file(self, file_name=None):
        if self._current_path.is_file():
            return self._current_path
        else:
            if file_name:
                file_path = Path(self._current_path,file_name)
                if file_path.is_file():
                    return file_path
                
        raise Exception('No file specified')
    
    async def save_file(self,file,file_name,file_path=None):
        file_path = file_path if file_path else self._current_path 
        path = Path(file_path,file_name)
        path.write_bytes(file)
        return path
    