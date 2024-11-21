from flask import request, jsonify  
from sqlalchemy.orm import joinedload  
from app import app, db  
from models import Fakultas, Prodi, Mahasiswa  


@app.route('/api/fakultas', methods=['GET'])
def get_fakultas():
    fakultas = Fakultas.query.options(joinedload(Fakultas.prodis)).all()
    
    output = []
    
    for fac in fakultas: 
        prodi_list = [{'id': prodi.id, 'nama': prodi.nama} for prodi in fac.prodis]
        output.append({
            'id': fac.id,
            'nama': fac.nama,
            'prodi': prodi_list
        })

    return jsonify(output)

# Route POST untuk Fakultas
@app.route('/api/fakultas', methods=['POST']) # Endpoint untuk menambahkan Fakultas baru
def add_fakultas():
    data = request.get_json() # Mendapatkan data JSON dari body request
    if 'nama' not in data: # Validasi jika data tidak memiliki key `nama`
        return jsonify({'message': 'Nama fakultas diperlukan'}), 400 # Mengembalikan error jika validasi gagal
    fakultas = Fakultas(nama=data['nama']) # Membuat objek Fakultas baru
    db.session.add(fakultas) # Menambahkan data Fakultas ke session database
    db.session.commit() # Menyimpan perubahan ke database
    return jsonify({'message': 'Fakultas berhasil ditambahkan'}), 201 # Mengembalikan pesan berhasil


