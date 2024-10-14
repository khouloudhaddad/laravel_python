<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Data;

class DataController extends Controller
{
    /**
     * Display a listing of the data.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function index()
    {
        $data = Data::all(); // Retrieve all records from the 'data' table
        return response()->json($data);
    }

    /**
     * Store a newly created data in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function store(Request $request)
    {
        $validatedData = $request->validate([
            'key' => 'required|string|max:255',
            'value' => 'required|string',
        ]);

        $data = Data::create($validatedData); // Create a new record
        return response()->json($data, 201); // Return the created record with a 201 status code
    }
}
